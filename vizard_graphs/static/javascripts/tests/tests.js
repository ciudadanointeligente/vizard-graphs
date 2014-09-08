QUnit.module("Basics",{
	"setup": function(){

	},
	"teardown": function(){

	}
})
QUnit.test("There is a class that instanciated creates everythign", function(assert){
	var mapper = new VizardMapper($("#testing_graph"))
	assert.ok(mapper)
	//the components
	assert.ok(mapper.graph)
	assert.ok(mapper.graph instanceof joint.dia.Graph)
	assert.ok(mapper.paper)
	assert.equal(mapper.paper.model, mapper.graph)
	assert.ok(mapper.paper instanceof joint.dia.Paper)
	assert.ok(mapper.stencil)
	assert.equal(mapper.stencil.options.paper, mapper.paper)
	assert.equal(mapper.stencil.options.graph, mapper.graph)
	assert.ok(mapper.stencil instanceof joint.ui.Stencil)
	assert.ok(mapper.paper_scroller instanceof joint.ui.PaperScroller)
	assert.equal(mapper.paper_scroller.options.paper, mapper.paper)

	assert.equal(mapper.stencil.getGraph().getElements().length, 1)
	var the_first_element =mapper.stencil.getGraph().getElements()[0]
	assert.ok(the_first_element instanceof joint.shapes.basic.Rect );

	mapper.remove()
})
QUnit.module("Drawing", {
	"setup": function(){
		this.mapper = new VizardMapper($("#testing_graph"));
	},
	"teardown": function(){
		this.mapper.remove()
	}
})
QUnit.test("Creates elements that are going to be used in the future", function(assert){
	var el = $("#testing_graph");
	assert.ok(el)
	assert.equal(el.find("div.vizard-stencil").length, 1)
	assert.equal(el.find("div.vizard-paper").length, 1)
})
QUnit.asyncTest( "Add element to graph", function( assert ) {
	expect(2)
	this.mapper.on("mapper:addElement", function(cell){
		assert.ok(true, "This callback was called")
		assert.ok(cell instanceof joint.shapes.basic.Rect)
	})
	QUnit.start()
	var rect = new joint.shapes.basic.Rect();
	this.mapper.graph.addCell(rect)
});