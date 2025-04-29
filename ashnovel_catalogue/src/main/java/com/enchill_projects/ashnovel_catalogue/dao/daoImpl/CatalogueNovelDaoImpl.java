/**
 * Implementation of Novel Data Access Object
 *
 * @author Emmanuel Enchill
 */
package com.enchill_projects.ashnovel_catalogue.dao.daoImpl;

import com.enchill_projects.ashnovel_catalogue.dao.CatalogueNovelDao;
import com.enchill_projects.ashnovel_catalogue.domain.Novel;
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
     * Add New Novel:
     * persists a new novel object to the database
     * @param novel the Novel object
     */
    public void addNewNovel(Novel novel) {
        Session session = sessionFactory.getCurrentSession();
        session.persist(novel);
    }
}
