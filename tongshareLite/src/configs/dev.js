//configuration for develop environment
module.exports = function (app, express) {
  app.configure('development', function(){
    app.use(express.errorHandler({ dumpExceptions: true, showStack: true })); 
  });
}
