/**
 * Page to record new novel
 *
 * @author Emmanuel Enchill
 */
package com.enchill_projects.ashnovel_catalogue.controller;

import com.enchill_projects.ashnovel_catalogue.domain.CatalogueNovel;
import com.enchill_projects.ashnovel_catalogue.service.CatalogueFileStorageService;
import com.enchill_projects.ashnovel_catalogue.service.CatalogueNovelService;

import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@Controller
@RequestMapping("catalogue")
public class CatalogueNovelController {

    private final CatalogueNovelService catalogueNovelService;
    private final CatalogueFileStorageService fileStorageService;

    @Autowired
    public CatalogueNovelController(CatalogueNovelService catalogueNovelService, CatalogueFileStorageService fileStorageService) {
        this.catalogueNovelService = catalogueNovelService;
        this.fileStorageService = fileStorageService;
    }

    /**
     * New CatalogueNovel:
     * display the form to add new novel record
     * @param model the model object
     * @return the template name of the form
     */
    @GetMapping("/new_novel")
    public String showNewNovelForm(Model model) {

        model.addAttribute("catalogueNovel", new CatalogueNovel());

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
            @Valid @ModelAttribute("catalogueNovel") CatalogueNovel catalogueNovel,
            BindingResult bindingResult,
            @RequestParam(value = "coverImage", required = false) MultipartFile coverImage,
            RedirectAttributes redirectAttributes) {

        if (bindingResult.hasErrors())
            return "new_novel";

        // Handle file upload
        try {

            if (!coverImage.isEmpty()) {
                String fileName = fileStorageService.storeFile(coverImage);
                catalogueNovel.setImagePath(fileName);
            }

            catalogueNovelService.saveNovelRecord(catalogueNovel);
            redirectAttributes.addFlashAttribute("success", "CatalogueNovel record saved successfully");
        } catch (RuntimeException exception) {
            redirectAttributes.addFlashAttribute("error", exception.getMessage());

            return "redirect:/catalogue/new_novel";
        }

        return "redirect:/catalogue/home";
    }

    /**
     * Novel Details:
     * get the details of a Novel object
     * @param id the id of the object
     * @param model the Novel model
     * @return the logical template name of the details page
     */
    @GetMapping("/{id}")
    public String getNovelDetailsById(@PathVariable("id") int id, Model model) {

        CatalogueNovel catalogueNovel = this.catalogueNovelService.getNovelById(id);
        model.addAttribute("novel", catalogueNovel);

        return "novel_details";
    }
}
