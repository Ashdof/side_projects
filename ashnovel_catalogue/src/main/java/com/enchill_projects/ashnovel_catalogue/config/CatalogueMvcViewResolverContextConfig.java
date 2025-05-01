/**
 * Configurations for Thymeleaf, View Resolver Engine and static resources
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.converter.HttpMessageConverter;
import org.springframework.http.converter.StringHttpMessageConverter;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.springframework.web.multipart.support.StandardServletMultipartResolver;

import org.thymeleaf.spring6.SpringTemplateEngine;
import org.thymeleaf.spring6.templateresolver.SpringResourceTemplateResolver;
import org.thymeleaf.spring6.view.ThymeleafViewResolver;
import org.thymeleaf.templatemode.TemplateMode;
import org.thymeleaf.templateresolver.ITemplateResolver;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Configuration
@EnableWebMvc
@ComponentScan("com.enchill_projects.ashnovel_catalogue")
public class CatalogueMvcViewResolverContextConfig implements WebMvcConfigurer {

    /**
     * Templates Path:
     * configuration for the path of the templates
     * @return the template resolver object
     */
    @Bean
    public SpringResourceTemplateResolver templateResolver() {

        SpringResourceTemplateResolver resolver = new SpringResourceTemplateResolver();
        resolver.setPrefix("classpath:/templates/");
        resolver.setSuffix(".html");
        resolver.setTemplateMode(TemplateMode.HTML);
        resolver.setCharacterEncoding("UTF-8");

        return resolver;
    }

    /**
     * Template Engine:
     * configuration for template engine resolver
     * @return the template engine object
     */
    @Bean
    public SpringTemplateEngine templateEngine() {

        SpringTemplateEngine templateEngine = new SpringTemplateEngine();

        Set<ITemplateResolver> iTemplateResolvers = new HashSet<>();
        iTemplateResolvers.add(templateResolver());

        templateEngine.setTemplateResolvers(iTemplateResolvers);

        return templateEngine;
    }

    @Bean
    public ThymeleafViewResolver thymeleafViewResolver() {
        ThymeleafViewResolver resolver = new ThymeleafViewResolver();

        resolver.setTemplateEngine(templateEngine());
        resolver.setCharacterEncoding("UTF-8");
        resolver.setCache(false);

        return resolver;
    }

    /**
     * Resource Location:
     * configuration for the location of static and template resources
     * @param registry the resource handler registry object
     */
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/resources/**")
                .addResourceLocations("/resources/");
    }

    /**
     * Configures the HTTP message converters used for request/response processing.
     *
     * This implementation:
     * 1. Clears all default converters that Spring autoconfigures (including JSON converters)
     * 2. Only registers the StringHttpMessageConverter which handles basic text content
     *
     * Why we do this:
     * - Prevents Spring from autoconfiguring JSON converters we don't need
     * - Eliminates the requirement for JSON-B (Yasson) or Jackson dependencies
     * - Reduces application startup time by only loading necessary converters
     * - Still maintains support for basic text processing required by Thymeleaf
     *
     * @param converters The list of converters to modify (initially contains Spring defaults)
     */
    @Override
    public void configureMessageConverters(List<HttpMessageConverter<?>> converters) {
        // Clear all default converters
        converters.clear();

        // Add only what you need (e.g., for Thymeleaf)
        converters.add(new StringHttpMessageConverter());
    }

    /**
     * Handler for multipart requests (image files etc.)
     * @return a resolver object for multipart requests
     */
    @Bean
    public StandardServletMultipartResolver multipartResolver() {
        return new StandardServletMultipartResolver();
    }
}
