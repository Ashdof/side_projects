/**
 * Unit Test Service
 *
 * @author Emmanuel Enchill
 */

package com.enchill_projects.ashnovel_catalogue.service;

import com.enchill_projects.ashnovel_catalogue.dao.CatalogueNovelDao;

import com.enchill_projects.ashnovel_catalogue.domain.CatalogueNovel;
import com.enchill_projects.ashnovel_catalogue.service.impl.CatalogueNovelServiceImpl;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
public class CatalogueNovelServiceTest {

    private CatalogueNovel catalogueNovel, catalogueNovel1;

    @Mock
    private CatalogueNovelDao catalogueNovelDao;

    @InjectMocks
    private CatalogueNovelServiceImpl catalogueNovelService;

    @BeforeEach
    void setUp() {

        catalogueNovel = new CatalogueNovel();
        catalogueNovel.setId(1L);
        catalogueNovel.setTitle("My Own Novel I");
        catalogueNovel.setAuthor("My Own Name");
        catalogueNovel.setGenre("Fantasy");
        catalogueNovel.setIsbn("0-345-09-098");
        catalogueNovel.setPubYear(LocalDate.now());
        catalogueNovel.setSummary("An interesting novel.");
        catalogueNovel.setPubCompany("My Own Company");
        catalogueNovel.setImagePath("none");
        catalogueNovel.setCreatedAt(LocalDateTime.now());
        catalogueNovel.setUpdatedAt(LocalDateTime.now());

        catalogueNovel1 = new CatalogueNovel();
        catalogueNovel1.setId(2L);
        catalogueNovel1.setTitle("My Own Novel II");
        catalogueNovel1.setAuthor("My Own Name");
        catalogueNovel1.setGenre("Fantasy");
        catalogueNovel1.setIsbn("0-355-10-099");
        catalogueNovel1.setPubYear(LocalDate.now());
        catalogueNovel1.setSummary("An interesting novel.");
        catalogueNovel1.setPubCompany("My Own Company");
        catalogueNovel1.setImagePath("none");
        catalogueNovel1.setCreatedAt(LocalDateTime.now());
        catalogueNovel1.setUpdatedAt(LocalDateTime.now());
    }

    @Test
    void getAllNovels_ShouldReturnAllNovels() {
        when(catalogueNovelDao.fetchAllNovels()).thenReturn(List.of(catalogueNovel, catalogueNovel1));

        // Act
        List<CatalogueNovel> catalogueNovels = catalogueNovelService.getAllNovelRecords();

        assertEquals(2, catalogueNovels.size());
        verify(catalogueNovelDao, times(1)).fetchAllNovels();
    }
}
