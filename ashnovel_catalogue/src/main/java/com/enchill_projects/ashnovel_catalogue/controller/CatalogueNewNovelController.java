/**
 * Page to record new novel
 *
 * @author Emmanuel Enchill
 */
package com.enchill_projects.ashnovel_catalogue.controller;

import com.enchill_projects.ashnovel_catalogue.domain.CatalogueNovel;
import com.enchill_projects.ashnovel_catalogue.service.CatalogueNovelService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
@RequestMapping("catalogue")
public class CatalogueNewNovelController {

    private final CatalogueNovelService catalogueNovelService;

    @Autowired
    public CatalogueNewNovelController(CatalogueNovelService catalogueNovelService) {
        this.catalogueNovelService = catalogueNovelService;
    }

    /**
     * New CatalogueNovel:
     * display the form to add new novel record
     * @param model the model object
     * @return the template name of the form
     */
    @GetMapping("/new_novel")
    public String showNewNovelForm(Model model) {

        model.addAttribute("novel", new CatalogueNovel());

        return "new_novel";
    }

    /**
     * Process Form:
     * process the form values and commit to the database
     * @param catalogueNovel the new CatalogueNovel object
     * @param bindingResult the binding object
     * @return to the home page if successful, otherwise remain on
     * the form if there are errors
     */
    @PostMapping("/new_novel")
    public String processNewNovelForm(
            @ModelAttribute("catalogueNovel") CatalogueNovel catalogueNovel,
            BindingResult bindingResult,
            RedirectAttributes redirectAttributes) {

        if (bindingResult.hasErrors())
            return "new_novel";

        catalogueNovelService.saveNovelRecord(catalogueNovel);
        redirectAttributes.addAttribute("success", "CatalogueNovel record saved successfully");

        return "redirect:/catalogue/home";
    }
}
