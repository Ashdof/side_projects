/**
 * Dispatcher Servlet Configuration
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.config;

import org.springframework.web.servlet.support.AbstractAnnotationConfigDispatcherServletInitializer;

public class CatalogueDispatcherServletInitializer extends AbstractAnnotationConfigDispatcherServletInitializer {

    /**
     * Data Connection:
     * configuration for the database connection source
     * @return the configuration objects
     */
    @Override
    public Class<?>[] getRootConfigClasses() {
        return new Class<?>[] {
                CatalogueRootApplicationContextConfig.class
        };
    }

    /**
     * View Resolver:
     * configuration classes for view resolvers
     * @return the view resolver objects
     */
    @Override
    public Class<?>[] getServletConfigClasses() {
        return new Class<?>[] {
                CatalogueMvcViewResolverContextConfig.class
        };
    }

    /**
     * Request Mapping:
     * configuration for request mapping
     * @return mapping object for all requests
     */
    @Override
    public String[] getServletMappings() {
        return new String[] { "/" };
    }
}
