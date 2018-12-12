let gulp            = require('gulp');
let $               = require('gulp-load-plugins')();
let browserSync     = require('browser-sync').create();
let exec            = require('child_process').exec;
let spawn           = require('child_process').spawn;
let cleanCSS        = require('gulp-clean-css');
let log             = require('fancy-log');
let c               = require('ansi-colors');
let reload          = browserSync.reload;

const src             = 'seeker/static_src/';
const dist            = 'seeker/static_src/dist/';
const ignore          = ['!node_modules'];

// +++++++++++++++++++++++++++++++++++++++
// Gulp tasks to build static assets
// +++++++++++++++++++++++++++++++++++++++

function errorAlert(err) {
  log(c.red(err.toString()));
  this.emit("end");
}

// Styles
gulp.task('css', function() {
  return gulp.src(src + 'css/style.scss')
  .pipe($.plumber({errorHandler: errorAlert}))
  .pipe($.sourcemaps.init())
  .pipe(cleanCSS({compatibility: 'ie11'}))
  .pipe($.sourcemaps.write('.'))
  .pipe(gulp.dest(dist + 'css/'))
  .pipe(browserSync.stream());
});

// Scripts
gulp.task('js', function() {
  return gulp.src([
    '../node_modules/jquery/dist/jquery.min.js',
    '../node_modules/bootstrap/dist/js/bootstrap.bundle.js',
    src + 'js/**.js'
  ])
  .pipe($.plumber({errorHandler: errorAlert}))
  .pipe($.concat('main.min.js'))
  .pipe($.uglify())
  .pipe(gulp.dest(dist + 'js/'))
  .pipe(browserSync.stream());
});

// Move Images
gulp.task('images', function() {
  return gulp.src(src + 'img/**/**')
  .pipe(gulp.dest(dist + 'img'))
  .pipe(browserSync.stream());
})

//  Build static assets
gulp.task('build',['css','js','images']);

// Deafult Gulp Task
gulp.task('default', ['runserver'], function() {
    browserSync.init({
        notify: true,
        online: true,
        injectChanges: true,
        proxy: "localhost:8000",
        open: false
    });
    gulp.watch(ignore, ['/**/**/**/**/*.{html,py}'], reload);
    gulp.watch(src + 'css/**/*.scss', ['css', reload]);
    gulp.watch(src + 'js/**/*.js', ['js', reload]);
});

// Start Virtualenv and start server
gulp.task('runserver', function() {
  var cmd = spawn('python3', ['manage.py', 'runserver'], {stdio: 'inherit'});
  cmd.on('close', function(code) {
    console.log('runServer exited with code ' + code);
    cb(code);
  });
});
