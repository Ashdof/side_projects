/**
 * Image File storage interface
 *
 * @author Emmanuel Enchill
 */
package com.enchill_projects.ashnovel_catalogue.service;

import org.springframework.core.io.Resource;
import org.springframework.web.multipart.MultipartFile;

public interface CatalogueFileStorageService {
    String storeFile(MultipartFile file);
    Resource loadFileAsResource(String filename);
}
