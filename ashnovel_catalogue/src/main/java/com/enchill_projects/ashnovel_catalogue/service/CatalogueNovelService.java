/**
 * Service interface for Novel repository
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.service;

import com.enchill_projects.ashnovel_catalogue.domain.Novel;

public interface CatalogueNovelService {
    void saveNovelRecord(Novel novel);
}
