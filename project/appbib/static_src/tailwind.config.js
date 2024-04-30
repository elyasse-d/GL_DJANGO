/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            fontFamily: {
              helvetica: ['Helvetica', 'Arial', 'sans-serif', 'regular'],
              'helvetica-65-medium': ['Helvetica Neue', 'Arial', 'sans-serif', '65-medium'],
              'helvetica-ultra-light': ['Helvetica Neue', 'Arial', 'sans-serif', 'ultra-light'],
              'helvetica-light-condensed': ['Helvetica Neue', 'Arial', 'sans-serif', 'light condensed'],
              preosper: ['Preospe'],
              nexus: ['Nexusbold','regular'],
            },
            fontSize: {
                'btn': '1.5625rem',
                'reg': '1.5rem',
                'title': '26rem',
                'light': '1.75rem',
                'logo': '3rem'
            },
            boxShadow: {
                'nav':'0 8px 0 rgba(158, 152, 152, 0.11)'
            },
            colors: {
                ired:'#C72E25',
                iblack:'#1D1D1D',
                iiblack:'#212121',
                iiwhite:'#ECECEC',
                iwhite:'#FEFFFE',
                shadow:'#9E9898',
            },
            letterSpacing: {
                'title':'0.08em',
            },
          },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
