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
              'helvetica-black': ['HelveticaNeue-Heavy'],
              'helvetica-ultra-light': ['Helvetica Neue','Light'],
              'helvetica-light-condensed': ['Helvetica Neue',  'light condensed'],
              preosper: ['Preospe'],
              nexus: ['Nexusbold','regular'],
            },
            fontSize: {
                'btn': '1.5625rem',
                'reg': '1.5rem',
                'title': '32rem',
                'light': '1.75rem',
                'logo': '3rem'
            },
            boxShadow: {
                'nav':'0 8px 0 rgba(158, 152, 152, 0.11)',
                
            },
            colors: {
                ired:'#C72E25',
                iblack:'#1D1D1D',
                iiblack:'#212121',
                iiwhite:'#ECECEC',
                iwhite:'#FEFFFE',
                shadow:'#9E9898',
                ishadow:'#585757',
                iborder:'rgba(158, 152, 152, 0.11)',
            },
            letterSpacing: {
                'title':'0.08em',
            },
            spacing:{
                'xf':'302px',
                'w':'311px',
                'hs':'499px',
                'img':'331px',
            },
            backgroundImage:{
                'login':"url('static/appbib/books.png')",
            },
          },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        // require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
