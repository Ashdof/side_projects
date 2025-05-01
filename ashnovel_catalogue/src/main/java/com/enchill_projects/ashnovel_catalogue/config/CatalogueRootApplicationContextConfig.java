/**
 * Configuration for database connectivity
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.config;

import org.hibernate.SessionFactory;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.support.PropertiesLoaderUtils;
import org.springframework.jdbc.datasource.DriverManagerDataSource;
import org.springframework.orm.hibernate5.HibernateTransactionManager;
import org.springframework.orm.hibernate5.LocalSessionFactoryBean;
import org.springframework.transaction.annotation.EnableTransactionManagement;

import javax.sql.DataSource;
import java.io.IOException;
import java.util.Properties;

@Configuration
@EnableTransactionManagement
@ComponentScan("com.enchill_projects.ashnovel_catalogue")
public class CatalogueRootApplicationContextConfig {

    /**
     * Database Connection:
     * a bean to create a connection to the database
     * @return the database connection object
     * @throws IOException if an error occurs
     */
    @Bean
    public DataSource dataSource() throws IOException {

        Properties properties;
        DriverManagerDataSource managerDataSource;

        managerDataSource = new DriverManagerDataSource();
        properties = PropertiesLoaderUtils.loadProperties(new ClassPathResource("db/db.properties"));

        managerDataSource.setDriverClassName(properties.getProperty("db.driver"));
        managerDataSource.setUrl(properties.getProperty("db.url"));
        managerDataSource.setUsername(properties.getProperty("db.username"));
        managerDataSource.setPassword(properties.getProperty("db.password"));

        return managerDataSource;
    }

    /**
     * Hibernate Session:
     * configuration for hibernate session
     * @return a session factory manager object
     * @throws IOException if an error occurs
     */
    @Bean
    public LocalSessionFactoryBean localSessionFactoryBean() throws IOException {

        LocalSessionFactoryBean sessionFactoryBean = new LocalSessionFactoryBean();
        sessionFactoryBean.setDataSource(this.dataSource());

        // Scan for model
        sessionFactoryBean.setPackagesToScan(
                "com.enchill_projects.ashnovel_catalogue.domain"
        );

        // Setup Hibernate properties
        Properties hibernateProperties = new Properties();
        hibernateProperties.setProperty("hibernate.dialect", "org.hibernate.dialect.PostgreSQLDialect");
        hibernateProperties.setProperty("hibernate.hbm2ddl.auto", "create");
        hibernateProperties.setProperty("hibernate.show_sql", "true"); // Prints executed SQL commands in terminal
        hibernateProperties.setProperty("hibernate.format_sql", "true");
        hibernateProperties.setProperty("hibernate.use_sql_comments", "true");

        sessionFactoryBean.setHibernateProperties(hibernateProperties);
        return sessionFactoryBean;
    }

    /**
     * Transaction Manager:
     * configuration for managing database transactions
     * @param sessionFactory the session object
     * @return a transaction manager object
     */
    @Bean
    public HibernateTransactionManager transactionManager(SessionFactory sessionFactory) {

        HibernateTransactionManager hibernateTransactionManager = new HibernateTransactionManager();
        hibernateTransactionManager.setSessionFactory(sessionFactory);

        return hibernateTransactionManager;
    }
}
