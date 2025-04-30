/**
 * A class to mode a Novel
 *
 * @author Emmanuel Enchill
 */
package com.enchill_projects.ashnovel_catalogue.domain;

import com.enchill_projects.ashnovel_catalogue.service.impl.CatalogueIdServiceImp;
import jakarta.persistence.*;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

@Entity
@Table(name = "novels")
public class Novel {

    @Id
    @Column(name = "novel_id", nullable = false, unique = true, updatable = false)
    private String id;

    @Column(name = "novel_title", nullable = false)
    private String title;

    @Column(name = "novel_author", nullable = false)
    private String author;

    @Column(name = "novel_genres", nullable = false)
    private List<String> genre;

    @Column(name = "novel_isbn", nullable = false)
    private String isbn;

    @Column(name = "date_published", nullable = false)
    private LocalDate pubYear;

    @Column(name = "novel_summary", nullable = false)
    private String summary;

    @Column(name = "publication_companies", nullable = false)
    private String pubCompanies;

    @Column(name = "imagePath", nullable = false)
    private String imagePath;

    @Column(name = "created_at", nullable = false)
    private LocalDateTime createdAt;

    @Column(name = "updated_at", nullable = false)
    private LocalDateTime updatedAt;

    private static final String DEFAULT_TEXT_VALUE = "none";

    /**
     * Default constructor:
     * create a new Novel object with default values
     */
    public Novel() {
        this.id = new CatalogueIdServiceImp().generateKsuidNewId();
        this.title = DEFAULT_TEXT_VALUE;
        this.author = DEFAULT_TEXT_VALUE;
        this.genre = new ArrayList<>(Collections.singleton(DEFAULT_TEXT_VALUE));
        this.isbn = DEFAULT_TEXT_VALUE;
        this.pubYear = LocalDate.now();
        this.pubCompanies = DEFAULT_TEXT_VALUE;
        this.createdAt = LocalDateTime.now();
        this.updatedAt = LocalDateTime.now();
    }

    /**
     * New Novel:
     * create a new Novel object with basic data
     * @param id the id  of the Novel
     * @param title the title of the Novel
     * @param author the author of the Novel
     * @param genre the Novel's genre(s)
     */
    public Novel(String id, String title, String author, List<String> genre) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.genre = genre;
    }

    public String getId() {
        return id;
    }

    public String getAuthor() {
        return author;
    }

    public String getTitle() {
        return title;
    }

    public List<String> getGenre() {
        return genre;
    }

    public String getIsbn() {
        return isbn;
    }

    public String getPubCompanies() {
        return pubCompanies;
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

    public void setId(String id) {

        if (id == null || id.isEmpty())
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
            throw new IllegalArgumentException("Title of Novel cannot be empty.");

        this.title = title;
    }

    public void setGenre(List<String> genre) {

        if (genre == null || genre.isEmpty())
            throw new IllegalArgumentException("Genres of Novel cannot be empty.");

        this.genre = genre;
    }

    public void setIsbn(String isbn) {

        if (isbn == null || isbn.isEmpty())
            throw new IllegalArgumentException("ISBN of Novel cannot be empty.");

        this.isbn = isbn;
    }

    public void setPubCompanies(String pubCompanies) {

        if (pubCompanies == null || pubCompanies.isEmpty())
            throw new IllegalArgumentException("Publication company cannot be empty.");

        this.pubCompanies = pubCompanies;
    }

    public void setPubYear(LocalDate pubYear) {

        if (pubYear == null || String.valueOf(pubYear).isEmpty())
            throw new IllegalArgumentException("Publication year cannot be empty.");

        this.pubYear = pubYear;
    }

    public void setSummary(String summary) {

        if (summary == null || summary.isEmpty())
            throw new IllegalArgumentException("Summary of Novel cannot be empty.");

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
