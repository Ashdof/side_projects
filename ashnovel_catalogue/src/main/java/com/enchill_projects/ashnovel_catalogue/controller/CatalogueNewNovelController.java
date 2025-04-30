/**
 * Page to record new novel
 *
 * @author Emmanuel Enchill
 */
package com.enchill_projects.ashnovel_catalogue.controller;

import com.enchill_projects.ashnovel_catalogue.domain.Novel;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("catalogue")
public class CatalogueNewNovelController {

    /**
     * New Novel:
     * display the form to add new novel record
     * @param model the model object
     * @return the template name of the form
     */
    @GetMapping("/new_novel")
    public String showNewNovelForm(Model model) {

        model.addAttribute("newNovel", new Novel());

        return "new_novel";
    }
}
