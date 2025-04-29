/**
 * Implementation of id service interface
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.service.impl;

import com.enchill_projects.ashnovel_catalogue.service.CatalogueIdService;
import com.enchill_projects.ashnovel_catalogue.utility.CatalogueNewKsuid;

import org.springframework.stereotype.Service;

@Service
public class CatalogueIdServiceImp implements CatalogueIdService {

    @Override
    public String generateKsuidNewId() {

        return CatalogueNewKsuid.generateNewKsuid();
    }
}
