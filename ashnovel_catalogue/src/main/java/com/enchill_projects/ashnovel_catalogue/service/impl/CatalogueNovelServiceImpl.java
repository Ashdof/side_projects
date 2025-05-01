/**
 * Implementation of CatalogueNovel Dao service interface
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.service.impl;

import com.enchill_projects.ashnovel_catalogue.dao.CatalogueNovelDao;
import com.enchill_projects.ashnovel_catalogue.domain.CatalogueNovel;
import com.enchill_projects.ashnovel_catalogue.service.CatalogueNovelService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class CatalogueNovelServiceImpl implements CatalogueNovelService {

    private final CatalogueNovelDao catalogueNovelDao;

    @Autowired
    public CatalogueNovelServiceImpl(CatalogueNovelDao catalogueNovelDao) {
        this.catalogueNovelDao = catalogueNovelDao;
    }

    /**
     * Save Record:
     * save a new catalogueNovel object to the database
     * @param catalogueNovel the catalogueNovel object
     */
    @Override
    @Transactional
    public void saveNovelRecord(CatalogueNovel catalogueNovel) {
        this.catalogueNovelDao.save(catalogueNovel);
    }
}
