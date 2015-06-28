{expect} = require "chai"
utils = require "../../utils"

Patches = utils.require "renderer/glyph/patches"

base = utils.require "common/base"
{Collections} = base

describe "patches renderer module", ->

  describe "_set_index", ->
    p = Patches.View

    it "should have empty data", ->
      r = Collections('ColumnDataSource').create(
        {'data': {'xs': [[0, 10, 10, 0]], 'ys':[[0, 0, 10, 10]]}}
      )
      console.log(p)
      # This should fail, but instead just doesn't work.
      # Error message TypeError: undefined is not a function
      expect(p.set_data(r)).to.be.deep.equal []
