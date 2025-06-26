module.exports = function(eleventyConfig) {
    eleventyConfig.addPassthroughCopy('css')
    eleventyConfig.addPassthroughCopy('scripts')
    return {
      passthroughFileCopy: true
    }
  }