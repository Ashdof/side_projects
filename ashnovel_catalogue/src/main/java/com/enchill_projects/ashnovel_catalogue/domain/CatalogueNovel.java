/**
 * A class to mode a CatalogueNovel
 *
 * @author Emmanuel Enchill
 */
package com.enchill_projects.ashnovel_catalogue.domain;

import jakarta.persistence.*;

import java.time.LocalDate;
import java.time.LocalDateTime;

@Entity
@Table(name = "novels")
public class CatalogueNovel {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "novel_id")
    private Long id;

    @Column(name = "novel_title", nullable = false)
    private String title;

    @Column(name = "novel_author", nullable = false)
    private String author;

    @Column(name = "novel_genres", nullable = false)
    private String genre;

    @Column(name = "novel_isbn", nullable = false)
    private String isbn;

    @Column(name = "date_published", nullable = false)
    private LocalDate pubYear;

    @Column(name = "novel_summary", nullable = false)
    private String summary;

    @Column(name = "publication_companies", nullable = false)
    private String pubCompany;

    @Column(name = "image_path", nullable = false)
    private String imagePath;

    @Column(name = "created_at", nullable = false)
    private LocalDateTime createdAt;

    @Column(name = "updated_at", nullable = false)
    private LocalDateTime updatedAt;

    private static final String DEFAULT_TEXT_VALUE = "none";

    /**
     * Default constructor:
     * create a new CatalogueNovel object with default values
     */
    public CatalogueNovel() {
        this.title = DEFAULT_TEXT_VALUE;
        this.author = DEFAULT_TEXT_VALUE;
        this.genre = DEFAULT_TEXT_VALUE;
        this.isbn = DEFAULT_TEXT_VALUE;
        this.pubYear = LocalDate.now();
        this.pubCompany = DEFAULT_TEXT_VALUE;
        this.createdAt = LocalDateTime.now();
        this.updatedAt = LocalDateTime.now();
    }

    /**
     * New CatalogueNovel:
     * create a new CatalogueNovel object with basic data
     * @param id the id  of the CatalogueNovel
     * @param title the title of the CatalogueNovel
     * @param author the author of the CatalogueNovel
     * @param genre the CatalogueNovel's genre(s)
     */
    public CatalogueNovel(Long id, String title, String author, String genre) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.genre = genre;
    }

    public Long getId() {
        return id;
    }

    public String getAuthor() {
        return author;
    }

    public String getTitle() {
        return title;
    }

    public String getGenre() {
        return genre;
    }

    public String getIsbn() {
        return isbn;
    }

    public String getPubCompany() {
        return pubCompany;
    }

    public LocalDate getPubYear() {
        return pubYear;
    }

    public String getSummary() {
        return summary;
    }

    public String getImagePath() {
        return imagePath;
    }

    public LocalDateTime getUpdatedAt() {
        return updatedAt;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setId(Long id) {

        if (id == null || String.valueOf(id).isEmpty())
            throw new IllegalArgumentException("Id cannot be empty.");

        this.id = id;
    }

    public void setAuthor(String author) {

        if (author == null || author.isEmpty())
            throw new IllegalArgumentException("Author's name cannot be empty.");

        this.author = author;
    }

    public void setTitle(String title) {

        if (title == null || title.isEmpty())
            throw new IllegalArgumentException("Title of CatalogueNovel cannot be empty.");

        this.title = title;
    }

    public void setGenre(String genre) {

        if (genre == null || genre.isEmpty())
            throw new IllegalArgumentException("Genres of CatalogueNovel cannot be empty.");

        this.genre = genre;
    }

    public void setIsbn(String isbn) {

        if (isbn == null || isbn.isEmpty())
            throw new IllegalArgumentException("ISBN of CatalogueNovel cannot be empty.");

        this.isbn = isbn;
    }

    public void setPubCompany(String pubCompany) {

        if (pubCompany == null || pubCompany.isEmpty())
            throw new IllegalArgumentException("Publication company cannot be empty.");

        this.pubCompany = pubCompany;
    }

    public void setPubYear(LocalDate pubYear) {

        if (pubYear == null || String.valueOf(pubYear).isEmpty())
            throw new IllegalArgumentException("Publication year cannot be empty.");

        this.pubYear = pubYear;
    }

    public void setSummary(String summary) {

        if (summary == null || summary.isEmpty())
            throw new IllegalArgumentException("Summary of CatalogueNovel cannot be empty.");

        this.summary = summary;
    }

    public void setImagePath(String imagePath) {
        this.imagePath = imagePath;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

    public void setUpdatedAt(LocalDateTime updatedAt) {
        this.updatedAt = updatedAt;
    }

    @PrePersist
    public void prePersist() {
        LocalDateTime localDate = LocalDateTime.now();

        this.createdAt = localDate;
        this.updatedAt = localDate;
    }

    @PreUpdate
    public void preUpdate() {
        this.updatedAt = LocalDateTime.now();
    }

}
