/**
 * Image File storage interface
 *
 * @author Emmanuel Enchill
 */
package com.enchill_projects.ashnovel_catalogue.service;

import org.springframework.web.multipart.MultipartFile;

public interface CatalogueFileStorageService {
    String store(MultipartFile file);
}
