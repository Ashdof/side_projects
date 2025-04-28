/**
 * Landing page controller
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("catalogue")
public class CatalogueHomeController {

    /**
     * Home page:
     * controller to display the home page
     * @return the logical template filename
     */
    @GetMapping("/home")
    public String showHomePage(Model model) {

        model.addAttribute("user", "jaykay");
        return "index";
    }
}
