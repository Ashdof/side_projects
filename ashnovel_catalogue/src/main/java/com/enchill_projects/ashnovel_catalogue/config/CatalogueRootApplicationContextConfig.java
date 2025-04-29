/**
 * Configuration for database connectivity
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.config;

import org.springframework.context.annotation.Bean;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.support.PropertiesLoaderUtils;
import org.springframework.jdbc.datasource.DriverManagerDataSource;

import javax.sql.DataSource;
import java.io.IOException;
import java.util.Properties;

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

    // Hibernate Configurations
    // PasswordEncoder Configurations etc.
}
