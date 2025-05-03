/**
 * Landing page controller
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.controller;

import com.enchill_projects.ashnovel_catalogue.domain.CatalogueNovel;
import com.enchill_projects.ashnovel_catalogue.service.CatalogueNovelService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.List;

@Controller
@RequestMapping("catalogue")
public class CatalogueHomeController {

    private final CatalogueNovelService catalogueNovelService;

    @Autowired
    public CatalogueHomeController(CatalogueNovelService catalogueNovelService) {
        this.catalogueNovelService = catalogueNovelService;
    }

    /**
     * Home page:
     * controller to display the home page
     * @return the logical template filename
     */
    @GetMapping("/home")
    public String showHomePage(Model model) {

        List<CatalogueNovel> catalogueNovels = this.catalogueNovelService.getAllNovelRecords();
        model.addAttribute("novels", catalogueNovels);

        return "index";
    }
}
