_ = require "underscore"
$ = require "jquery"

ContinuumView = require "../common/continuum_view"
HasProperties = require "../common/has_properties"

class ReloadingView extends ContinuumView
  initialize: (options) ->
    super(options)
    @$el.addClass("bk-reloading")
    @$el.empty()
    @$el.text("Reloading...")
    @render()

  render: () ->
    if @mget("visible")
       @$el.show()
    else
       @$el.hide()
    return @

class Reloading extends HasProperties
  type: "Reloading"
  default_view: ReloadingView

  defaults: () ->
    return _.extend {}, super(), {
      visible: false
    }

module.exports =
  Model: Reloading
  View: ReloadingView
