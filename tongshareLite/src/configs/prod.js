//configuration for production environment

module.exports = function (app, express) {
  app.configure('production', function(){
    app.use(express.errorHandler()); 
  });
}
