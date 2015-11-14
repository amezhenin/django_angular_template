var gulp = require('gulp');
var inject = require('gulp-inject');
var mainBowerFiles = require('main-bower-files');
var series = require('stream-series');
var autoprefixer = require('gulp-autoprefixer');
var runSequence = require('run-sequence');

gulp.task('default', function () {
  // place code for your default task here
  console.log(mainBowerFiles())
});


gulp.task('build', function (cb) {
  runSequence('index', 'autoprefix', cb);
});


gulp.task('autoprefix', function () {
  return gulp.src('./static/app/**/*.css')
    .pipe(autoprefixer({
      browsers: ['last 2 versions'],
      cascade: true
    }))
    .pipe(gulp.dest('./static/app/'));
});


gulp.task('index', function () {
  var target = gulp.src('./static/index.html');

  var vendor = gulp.src(mainBowerFiles(), {read: false});

  var sources = gulp.src([
    './static/app/services/*.js',
    './static/app/controllers/**/*.js',
    './static/app/*.js',
    './static/app/**/*.css'
  ], {read: false});

  return target
    .pipe(inject(series(vendor, sources)))
    .pipe(gulp.dest('./static'));
});

