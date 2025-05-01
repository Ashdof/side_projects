/**
 * Custom ID generator to be used in Hibernate
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.service.impl;

import com.enchill_projects.ashnovel_catalogue.service.CatalogueIdService;
import org.hibernate.engine.spi.SharedSessionContractImplementor;
import org.hibernate.id.IdentifierGenerator;
import org.springframework.beans.factory.annotation.Autowired;

import java.io.Serializable;

public class CatalogueIdGenerator implements IdentifierGenerator {

    private final CatalogueIdService catalogueIdService;

    @Autowired
    public CatalogueIdGenerator(CatalogueIdService catalogueIdService) {
        this.catalogueIdService = catalogueIdService;
    }

    @Override
    public Serializable generate(SharedSessionContractImplementor sessionContractImplementor, Object object) {
        return catalogueIdService.generateKsuidNewId();
    }
}
