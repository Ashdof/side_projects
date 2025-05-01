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
import java.net.MalformedURLException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.Arrays;
import java.util.Objects;
import java.util.UUID;

@Service
public class CatalogueFileStorageServiceImp implements CatalogueFileStorageService {

    private final Path fileStorageLocation;
    private final String[] allowedContentTypes;

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
        this.allowedContentTypes = allowedTypes.split(",");

        try {
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
        if (!Arrays.asList(allowedContentTypes).contains(file.getContentType()))
            throw new RuntimeException("Invalid file type");

        // Generate unique file name
        String originalFileName = StringUtils.cleanPath(Objects.requireNonNull(file.getOriginalFilename()));
        String fileExtension = originalFileName.substring(originalFileName.lastIndexOf("."));
        String newFileName = UUID.randomUUID() + fileExtension;

        try {

            // Copy file to target directory
            Path targetLocation = this.fileStorageLocation.resolve(newFileName);
            Files.copy(file.getInputStream(), targetLocation, StandardCopyOption.REPLACE_EXISTING);

            return newFileName;
        } catch (IOException exception) {
            throw new RuntimeException("Failed to upload file - " + exception.getMessage());
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
