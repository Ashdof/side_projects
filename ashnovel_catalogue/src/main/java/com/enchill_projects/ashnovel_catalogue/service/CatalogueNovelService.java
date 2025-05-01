/**
 * Service interface for CatalogueNovel repository
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.service;

import com.enchill_projects.ashnovel_catalogue.domain.CatalogueNovel;

public interface CatalogueNovelService {
    void saveNovelRecord(CatalogueNovel catalogueNovel);
}
