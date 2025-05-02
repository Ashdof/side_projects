/**
 * Implementation of CatalogueNovel Data Access Object
 *
 * @author Emmanuel Enchill
 */
package com.enchill_projects.ashnovel_catalogue.dao.daoImpl;

import com.enchill_projects.ashnovel_catalogue.dao.CatalogueNovelDao;
import com.enchill_projects.ashnovel_catalogue.domain.CatalogueNovel;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class CatalogueNovelDaoImpl implements CatalogueNovelDao {

    private final SessionFactory sessionFactory;

    @Autowired
    public CatalogueNovelDaoImpl(SessionFactory sessionFactory) {
        this.sessionFactory = sessionFactory;
    }

    /**
     * Add New CatalogueNovel:
     * persists a new catalogueNovel object to the database
     * @param catalogueNovel the CatalogueNovel object
     */
    public void save(CatalogueNovel catalogueNovel) {
        Session session = sessionFactory.getCurrentSession();
        session.persist(catalogueNovel);
    }

    /**
     * All Novels:
     * get all Novel objects from the database
     * @return a list of all Novel objects
     */
    public List<CatalogueNovel> fetchAllNovels() {
        Session session = sessionFactory.openSession();
        List<CatalogueNovel> catalogueNovels;

        try {
            catalogueNovels = session.createQuery("FROM CatalogueNovel", CatalogueNovel.class).list();
        } finally {
            session.clear();
        }

        return catalogueNovels;
    }
}
