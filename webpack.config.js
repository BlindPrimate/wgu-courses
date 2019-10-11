const path = require('path');

module.exports = {
    mode: 'development',
    entry: {
        app: './apps/course_selector/static/js/app.js'
    },
    watch: true,
    devtool: 'source-map',
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'apps', 'course_selector', 'static', 'js', )
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: ['babel-loader']
            }
        ]
    },
    resolve: {
        extensions: [
            '.js'
        ]
    }
}