/**
 * Implementation of file storage service interface
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.service.impl;

import com.enchill_projects.ashnovel_catalogue.service.CatalogueFileStorageService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.Resource;
import org.springframework.core.io.UrlResource;
import org.springframework.stereotype.Service;
import org.springframework.util.StringUtils;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.*;
import java.util.stream.Collectors;

@Service
public class CatalogueFileStorageServiceImp implements CatalogueFileStorageService {

    private final Path fileStorageLocation;
    private final Set<String> allowedContentTypes;
    private final Set<String> allowedExtensions;

    /**
     * Initialize Storage:
     * initialize image file storage directory
     * @param uploadDir the path to the storage directory
     * @param allowedTypes the allowed image file types
     */
    @Autowired
    public CatalogueFileStorageServiceImp(
            @Value("${file.upload-dir}") String uploadDir,
            @Value("${file.allowed-types}") String allowedTypes) {

        this.fileStorageLocation = Paths.get(uploadDir).toAbsolutePath().normalize();

        // Process allowed types
        this.allowedContentTypes = Arrays.stream(allowedTypes.split(","))
                .map(String::trim)
                .map(String::toLowerCase)
                .collect(Collectors.toSet());

        // Check corresponding file extensions
        this.allowedExtensions = Set.of("jpg", "jpeg", "png", "gif");

        try {
            if (!Files.exists(fileStorageLocation.getParent()))
                Files.createDirectories(this.fileStorageLocation);
        } catch (Exception exception) {
            throw new RuntimeException("Error creating storage directories - " + exception.getMessage());
        }
    }

    /**
     * Store File:
     * upload the image file to the dedicated storage directory
     * @param file the image file to upload
     * @return the file name
     */
    @Override
    public String storeFile(MultipartFile file) {

        // Validate the file
        if (file.isEmpty())
            throw new RuntimeException("Error saving file: empty");

        // Check the content type of the file
        String contentType = Optional.ofNullable(file.getContentType())
                .orElse("")
                .trim()
                .toLowerCase();

        // Get the file extension
        String originalFileName = StringUtils.cleanPath(Objects.requireNonNull(file.getOriginalFilename()));
        String fileExtension = originalFileName.substring(originalFileName.lastIndexOf(".") + 1).toLowerCase();

        // Validate file content type
        if (!allowedContentTypes.contains(contentType)) {
            System.out.println("Content type received: " + contentType);
            System.out.println("Content type allowed: " + allowedContentTypes);

            throw new RuntimeException("Invalid content type");
        }

        // Validate file extension
        if (!allowedExtensions.contains(fileExtension)) {
            throw new RuntimeException(
                    String.format("Invalid file extension '%s'. Allowed extensions: [%s]%n",
                            fileExtension,
                            String.join(", ", Arrays.toString(allowedExtensions.toArray())))
            );
        }

        // Generate unique filename
        String newFileName = UUID.randomUUID() + "." + fileExtension;

        try {
            Path targetLocation = this.fileStorageLocation.resolve(newFileName);

            if (!Files.exists(targetLocation.getParent()))
                Files.createDirectories(targetLocation.getParent());

            // Copy file to target directory
            try(InputStream inputStream = file.getInputStream()) {
                Files.copy(inputStream, targetLocation, StandardCopyOption.REPLACE_EXISTING);
            }

            return newFileName;
        } catch (IOException exception) {
            String errorDetails = String.format(
                    "Failed to upload file [%s] to [%s]. Reason: %s%n",
                    file.getOriginalFilename(),
                    this.fileStorageLocation.resolve(newFileName),
                    exception.getMessage()
            );

            throw new RuntimeException("Failed to upload file - " + errorDetails);
        }
    }

    /**
     * Load Files:
     * loa the image file
     * @param filename the name of the image file
     * @return the image file
     */
    @Override
    public Resource loadFileAsResource(String filename) {

        try {
            Path filePath = this.fileStorageLocation.resolve(filename).normalize();
            Resource resource = new UrlResource(filePath.toUri());

            if (resource.exists())
                return resource;
            else
                throw new RuntimeException("File not found - " + filename);
        } catch (MalformedURLException exception) {
            throw new RuntimeException("File not found - " + filename, exception);
        }
    }
}
