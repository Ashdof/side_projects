/**
 * Novel repository interface
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.dao;

import com.enchill_projects.ashnovel_catalogue.domain.Novel;

public interface CatalogueNovelRepository {
    void addNewNovel(Novel novel);
}
