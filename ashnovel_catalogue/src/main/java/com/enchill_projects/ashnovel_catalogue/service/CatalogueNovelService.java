/**
 * Service interface for Novel repository
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.service;

import com.enchill_projects.ashnovel_catalogue.domain.Novel;
import org.springframework.stereotype.Service;

@Service
public interface CatalogueNovelService {
    void addNewNovelRecord(Novel novel);
}
