/**
 * Landing page controller
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.controller;

import com.enchill_projects.ashnovel_catalogue.service.CatalogueIdService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("catalogue")
public class CatalogueHomeController {

    private final CatalogueIdService catalogueIdService;

    @Autowired
    public CatalogueHomeController(CatalogueIdService catalogueIdService) {
        this.catalogueIdService = catalogueIdService;
    }

    /**
     * Home page:
     * controller to display the home page
     * @return the logical template filename
     */
    @GetMapping("/home")
    public String showHomePage(Model model) {

        String id = catalogueIdService.generateKsuidNewId();

        model.addAttribute("user", "jaykay");
        model.addAttribute("id", id);

        return "index";
    }
}
