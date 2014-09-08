var VizardMapper = function(el){
	this.el = el;
	
	if (this.el.find("div.vizard-stencil").length === 0){
		this.el.append('<div class="vizard-stencil"></div>')
	}
	if (this.el.find('div.vizard-paper').length === 0) {
		this.el.append('<div class="vizard-paper"></div>')	
	}
	
	this.initialize();
	this.populateStencil()
	this.el.find("div.vizard-paper").append(this.paper_scroller.render().el);
};
VizardMapper.prototype.initialize = function(){
	this.graph = new joint.dia.Graph();
	this.graph.on("add", this.newElementAdded.bind(this))
	this.paper = new joint.dia.Paper({
		'model' : this.graph
	});
	this.stencil = new joint.ui.Stencil({graph:this.graph, paper:this.paper});

	this.paper_scroller = new joint.ui.PaperScroller({
	    paper: this.paper
	});
}
VizardMapper.prototype.newElementAdded = function(cell){
	this.trigger("mapper:addElement", cell)
}

VizardMapper.prototype.populateStencil =  function(){
	this.el.find("div.vizard-stencil").append(this.stencil.render().el);
	var r = new joint.shapes.basic.Rect({ 
	    position: { x: 10, y: 10 }, size: { width: 50, height: 30 } 
	});

	this.stencil.load([r]);
	//
	joint.layout.GridLayout.layout(this.stencil.getGraph(), {
	    columns: 100,
	    columnWidth: 110,
	    rowHeight: 110,
	    dy: 20,
	    dx: 20,
	    resizeToFit: true
	});
	this.stencil.getPaper().fitToContent(0, 0, 10);

}
VizardMapper.prototype.remove = function(){
	this.paper_scroller.remove()
	this.paper.remove()
	this.stencil.remove()
	this.graph.clear()
}
_.extend(VizardMapper.prototype, Backbone.Events);