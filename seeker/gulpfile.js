var gulp            = require('gulp');
var $               = require('gulp-load-plugins')();
var browserSync     = require('browser-sync');
var gutil           = require('gulp-util');
var exec            = require('child_process').exec;
var spawn           = require('child_process').spawn;
var reload          = browserSync.reload;
var src             = 'seeker/static_src/';
var dist            = 'seeker/static_src/dist/';
var ignore          = ['!node_modules'];

// +++++++++++++++++++++++++++++++++++++++
// Gulp tasks to build static assets
// +++++++++++++++++++++++++++++++++++++++

function errorAlert(err) {
  $.notify.onError({
    title: "Gulp Error",
    message: "Check your terminal",
    sound: "Basso"
  })(err);
  gutil.log(gutil.colors.red(err.toString()));
  this.emit("end");
}

// Styles
gulp.task('css', function() {
  return gulp.src(src + 'css/style.scss')
  .pipe($.plumber({errorHandler: errorAlert}))
  .pipe($.sourcemaps.init())
  .pipe($.sass())
  .pipe($.autoprefixer({
      browsers: ['last 2 versions'],
      cascade: false }))
  .pipe($.cssnano())
  .pipe($.sourcemaps.write('.'))
  .pipe(gulp.dest(dist + 'css/'))
});

// Scripts
gulp.task('js', function() {
  return gulp.src([
    src + 'js/lib/**.js',
    src + 'js/**.js'
  ])
  .pipe($.plumber({errorHandler: errorAlert}))
  .pipe($.concat('main.min.js'))
  .pipe($.uglify())
  .pipe(gulp.dest(dist + 'js/'))
});

// Move Images
gulp.task('images', function() {
  return gulp.src(src + 'img/**/**')
  .pipe(gulp.dest(dist + 'img'))
})

//  Build static assets
gulp.task('build',['css','js','images']);

// Deafult Gulp Task
gulp.task('default',['runserver'], function() {
    browserSync.init({
        notify: true,
        online: false,
        injectChanges: true,
        proxy: "localhost:8000"
    });
    gulp.watch(ignore, ['/**/**/**/**/*.{html,py}'], reload);
    gulp.watch(src + 'css/**/*.scss', ['css', reload]);
    gulp.watch(src + 'js/**/*.js', ['js', reload]);
});

// Start Virtualenv and start server
gulp.task('runserver', function() {
  var proc;
  proc = exec('PYTHONUNBUFFERED=1 ./manage.py runserver');
  proc.stderr.on('data', function(data) {
    return process.stdout.write(data);
  });
});


// gulp.task('runserver', function(cb) {
//   var cmd = spawn('python', ['manage.py', 'runserver'], {stdio: 'inherit'});
//   cmd.on('close', function(code) {
//     console.log('runserver exited with code ' + code);
//     cb(code);
//   });
// });