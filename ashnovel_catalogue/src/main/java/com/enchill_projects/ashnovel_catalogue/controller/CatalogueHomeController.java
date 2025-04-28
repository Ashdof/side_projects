/**
 * Landing page controller
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class CatalogueHomeController {

    /**
     * Home page:
     * controller to display the home page
     * @return the logical template filename
     */
    @GetMapping("/catalogue")
    public String showHomePage() {

        return "index";
    }
}
