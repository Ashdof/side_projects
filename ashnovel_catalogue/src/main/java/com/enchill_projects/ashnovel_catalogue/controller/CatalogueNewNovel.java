/**
 * Page to record new novel
 *
 * @author Emmanuel Enchill
 */
package com.enchill_projects.ashnovel_catalogue.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class CatalogueNewNovel {

    /**
     * New Novel:
     * display the form to add new novel record
     * @param model the model object
     * @return the template name of the form
     */
    @GetMapping("/new_novel")
    public String showNewNovelForm(Model model) {

        model.addAttribute("user", "jaykay");

        return "new_novel";
    }
}
