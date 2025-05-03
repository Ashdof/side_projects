/**
 * Service interface for CatalogueNovel repository
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.service;

import com.enchill_projects.ashnovel_catalogue.domain.CatalogueNovel;

import java.util.List;

public interface CatalogueNovelService {
    void saveNovelRecord(CatalogueNovel catalogueNovel);
    List<CatalogueNovel> getAllNovelRecords();
}
