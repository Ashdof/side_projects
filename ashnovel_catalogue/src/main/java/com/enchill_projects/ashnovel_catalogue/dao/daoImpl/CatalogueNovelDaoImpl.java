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
}
