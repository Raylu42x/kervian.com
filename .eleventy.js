module.exports = function(eleventyConfig) {
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
