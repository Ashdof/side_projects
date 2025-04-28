/**
 * Configurations for Thymeleaf, View Resolver Engine and static resources
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.EnableWebMvc;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import org.thymeleaf.spring6.SpringTemplateEngine;
import org.thymeleaf.spring6.templateresolver.SpringResourceTemplateResolver;
import org.thymeleaf.templatemode.TemplateMode;
import org.thymeleaf.templateresolver.ITemplateResolver;

import java.util.HashSet;
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
}
