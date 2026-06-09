const markdownIt = require('markdown-it');
const md = markdownIt();

module.exports = function(eleventyConfig) {
  eleventyConfig.addFilter('markdown', (content) => md.render(content || ''));

  // Projects collection
  eleventyConfig.addCollection("projects", function(collectionApi) {
    return collectionApi.getAll().filter(item => (item.data.tags || []).includes("project"));
  });

  // Tutorials collection
  eleventyConfig.addCollection("tutorials", function(collectionApi) {
    return collectionApi.getAll().filter(item => (item.data.tags || []).includes("build"));
  });

  // Games collection
  eleventyConfig.addCollection("games", function(collectionApi) {
    return collectionApi.getAll().filter(item => {
      // Must be inside src/games/ AND not the index.md (Hub page)
      const isGameFolder = item.inputPath.includes("src/games/") &&
                          !item.inputPath.endsWith("index.md") &&
                          item.inputPath.endsWith("index.html");
      return isGameFolder;
    });
  });


  eleventyConfig.addGlobalData("year", () => new Date().getFullYear());

  // Passthrough copy for CSS
  eleventyConfig.addPassthroughCopy({"src/css": "css"});

  // Passthrough copy for games folder
  eleventyConfig.addPassthroughCopy({"src/games": "games"});

  // Passthrough copy for FLL 2025-26 site archive
  eleventyConfig.addPassthroughCopy({"src/projects/fll-2025-26/site": "projects/fll-2025-26/site"});

  // Passthrough copy for admin (Sveltia CMS)
  eleventyConfig.addPassthroughCopy({"src/admin": "admin"});

  // Passthrough copy for uploads (CMS media library)
  eleventyConfig.addPassthroughCopy({"src/uploads": "uploads"});

  return {
    dir: {
      input: "src",        // your source files
      output: "docs",      // <-- change here
      includes: "_includes",
      pathPrefix: "/"
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    dataTemplateEngine: "njk"
  };


};
