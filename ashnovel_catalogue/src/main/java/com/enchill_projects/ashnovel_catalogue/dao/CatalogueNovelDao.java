/**
 * CatalogueNovel repository interface
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.dao;

import com.enchill_projects.ashnovel_catalogue.domain.CatalogueNovel;

import java.util.List;

public interface CatalogueNovelDao {
    void save(CatalogueNovel catalogueNovel);
    List<CatalogueNovel> fetchAllNovels();
}
