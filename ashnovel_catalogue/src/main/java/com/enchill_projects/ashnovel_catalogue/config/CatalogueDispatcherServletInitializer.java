/**
 * Dispatcher Servlet Configuration
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.config;

import org.springframework.web.servlet.support.AbstractAnnotationConfigDispatcherServletInitializer;

import jakarta.servlet.MultipartConfigElement;
import jakarta.servlet.ServletRegistration;

public class CatalogueDispatcherServletInitializer extends AbstractAnnotationConfigDispatcherServletInitializer {

    /**
     * File Upload:
     * configuration for file uploads
     * @param registration the {@code DispatcherServlet} registration to be customized
     */
    @Override
    public void customizeRegistration(ServletRegistration.Dynamic registration) {
        MultipartConfigElement multipartConfigElement = new MultipartConfigElement(
                null,
                5242880,
                10485760,
                0
        );

        registration.setMultipartConfig(multipartConfigElement);
    }

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
