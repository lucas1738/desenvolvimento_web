import sublime_plugin
import sublime

# The following 2 lines can be generated with "grunt sublime" in the main bootstrap code
bootstrap_classes = ["active","affix","alert","alert-danger","alert-dismissable","alert-info","alert-link","alert-success","alert-warning","arrow","badge","bg-danger","bg-info","bg-primary","bg-success","bg-warning","blockquote-reverse","bottom","bottom-left","bottom-right","breadcrumb","btn","btn-block","btn-danger","btn-default","btn-group","btn-group-justified","btn-group-lg","btn-group-sm","btn-group-vertical","btn-group-xs","btn-info","btn-lg","btn-link","btn-primary","btn-sm","btn-success","btn-toolbar","btn-warning","btn-xs","caption","caret","carousel","carousel-caption","carousel-control","carousel-indicators","carousel-inner","center-block","checkbox","checkbox-inline","clearfix","close","col-lg-1","col-lg-10","col-lg-11","col-lg-12","col-lg-2","col-lg-3","col-lg-4","col-lg-5","col-lg-6","col-lg-7","col-lg-8","col-lg-9","col-lg-offset-0","col-lg-offset-1","col-lg-offset-10","col-lg-offset-11","col-lg-offset-12","col-lg-offset-2","col-lg-offset-3","col-lg-offset-4","col-lg-offset-5","col-lg-offset-6","col-lg-offset-7","col-lg-offset-8","col-lg-offset-9","col-lg-pull-0","col-lg-pull-1","col-lg-pull-10","col-lg-pull-11","col-lg-pull-12","col-lg-pull-2","col-lg-pull-3","col-lg-pull-4","col-lg-pull-5","col-lg-pull-6","col-lg-pull-7","col-lg-pull-8","col-lg-pull-9","col-lg-push-0","col-lg-push-1","col-lg-push-10","col-lg-push-11","col-lg-push-12","col-lg-push-2","col-lg-push-3","col-lg-push-4","col-lg-push-5","col-lg-push-6","col-lg-push-7","col-lg-push-8","col-lg-push-9","col-md-1","col-md-10","col-md-11","col-md-12","col-md-2","col-md-3","col-md-4","col-md-5","col-md-6","col-md-7","col-md-8","col-md-9","col-md-offset-0","col-md-offset-1","col-md-offset-10","col-md-offset-11","col-md-offset-12","col-md-offset-2","col-md-offset-3","col-md-offset-4","col-md-offset-5","col-md-offset-6","col-md-offset-7","col-md-offset-8","col-md-offset-9","col-md-pull-0","col-md-pull-1","col-md-pull-10","col-md-pull-11","col-md-pull-12","col-md-pull-2","col-md-pull-3","col-md-pull-4","col-md-pull-5","col-md-pull-6","col-md-pull-7","col-md-pull-8","col-md-pull-9","col-md-push-0","col-md-push-1","col-md-push-10","col-md-push-11","col-md-push-12","col-md-push-2","col-md-push-3","col-md-push-4","col-md-push-5","col-md-push-6","col-md-push-7","col-md-push-8","col-md-push-9","col-sm-1","col-sm-10","col-sm-11","col-sm-12","col-sm-2","col-sm-3","col-sm-4","col-sm-5","col-sm-6","col-sm-7","col-sm-8","col-sm-9","col-sm-offset-0","col-sm-offset-1","col-sm-offset-10","col-sm-offset-11","col-sm-offset-12","col-sm-offset-2","col-sm-offset-3","col-sm-offset-4","col-sm-offset-5","col-sm-offset-6","col-sm-offset-7","col-sm-offset-8","col-sm-offset-9","col-sm-pull-0","col-sm-pull-1","col-sm-pull-10","col-sm-pull-11","col-sm-pull-12","col-sm-pull-2","col-sm-pull-3","col-sm-pull-4","col-sm-pull-5","col-sm-pull-6","col-sm-pull-7","col-sm-pull-8","col-sm-pull-9","col-sm-push-0","col-sm-push-1","col-sm-push-10","col-sm-push-11","col-sm-push-12","col-sm-push-2","col-sm-push-3","col-sm-push-4","col-sm-push-5","col-sm-push-6","col-sm-push-7","col-sm-push-8","col-sm-push-9","col-xs-1","col-xs-10","col-xs-11","col-xs-12","col-xs-2","col-xs-3","col-xs-4","col-xs-5","col-xs-6","col-xs-7","col-xs-8","col-xs-9","col-xs-offset-0","col-xs-offset-1","col-xs-offset-10","col-xs-offset-11","col-xs-offset-12","col-xs-offset-2","col-xs-offset-3","col-xs-offset-4","col-xs-offset-5","col-xs-offset-6","col-xs-offset-7","col-xs-offset-8","col-xs-offset-9","col-xs-pull-0","col-xs-pull-1","col-xs-pull-10","col-xs-pull-11","col-xs-pull-12","col-xs-pull-2","col-xs-pull-3","col-xs-pull-4","col-xs-pull-5","col-xs-pull-6","col-xs-pull-7","col-xs-pull-8","col-xs-pull-9","col-xs-push-0","col-xs-push-1","col-xs-push-10","col-xs-push-11","col-xs-push-12","col-xs-push-2","col-xs-push-3","col-xs-push-4","col-xs-push-5","col-xs-push-6","col-xs-push-7","col-xs-push-8","col-xs-push-9","collapse","collapsing","container","container-fluid","control-label","danger","disabled","divider","dl-horizontal","dropdown","dropdown-backdrop","dropdown-header","dropdown-menu","dropdown-menu-left","dropdown-menu-right","dropdown-toggle","dropup","fade","form-control","form-control-feedback","form-control-static","form-group","form-horizontal","form-inline","glyphicon","glyphicon-adjust","glyphicon-align-center","glyphicon-align-justify","glyphicon-align-left","glyphicon-align-right","glyphicon-arrow-down","glyphicon-arrow-left","glyphicon-arrow-right","glyphicon-arrow-up","glyphicon-asterisk","glyphicon-backward","glyphicon-ban-circle","glyphicon-barcode","glyphicon-bell","glyphicon-bold","glyphicon-book","glyphicon-bookmark","glyphicon-briefcase","glyphicon-bullhorn","glyphicon-calendar","glyphicon-camera","glyphicon-certificate","glyphicon-check","glyphicon-chevron-down","glyphicon-chevron-left","glyphicon-chevron-right","glyphicon-chevron-up","glyphicon-circle-arrow-down","glyphicon-circle-arrow-left","glyphicon-circle-arrow-right","glyphicon-circle-arrow-up","glyphicon-cloud","glyphicon-cloud-download","glyphicon-cloud-upload","glyphicon-cog","glyphicon-collapse-down","glyphicon-collapse-up","glyphicon-comment","glyphicon-compressed","glyphicon-copyright-mark","glyphicon-credit-card","glyphicon-cutlery","glyphicon-dashboard","glyphicon-download","glyphicon-download-alt","glyphicon-earphone","glyphicon-edit","glyphicon-eject","glyphicon-envelope","glyphicon-euro","glyphicon-exclamation-sign","glyphicon-expand","glyphicon-export","glyphicon-eye-close","glyphicon-eye-open","glyphicon-facetime-video","glyphicon-fast-backward","glyphicon-fast-forward","glyphicon-file","glyphicon-film","glyphicon-filter","glyphicon-fire","glyphicon-flag","glyphicon-flash","glyphicon-floppy-disk","glyphicon-floppy-open","glyphicon-floppy-remove","glyphicon-floppy-save","glyphicon-floppy-saved","glyphicon-folder-close","glyphicon-folder-open","glyphicon-font","glyphicon-forward","glyphicon-fullscreen","glyphicon-gbp","glyphicon-gift","glyphicon-glass","glyphicon-globe","glyphicon-hand-down","glyphicon-hand-left","glyphicon-hand-right","glyphicon-hand-up","glyphicon-hd-video","glyphicon-hdd","glyphicon-header","glyphicon-headphones","glyphicon-heart","glyphicon-heart-empty","glyphicon-home","glyphicon-import","glyphicon-inbox","glyphicon-indent-left","glyphicon-indent-right","glyphicon-info-sign","glyphicon-italic","glyphicon-leaf","glyphicon-link","glyphicon-list","glyphicon-list-alt","glyphicon-lock","glyphicon-log-in","glyphicon-log-out","glyphicon-magnet","glyphicon-map-marker","glyphicon-minus","glyphicon-minus-sign","glyphicon-move","glyphicon-music","glyphicon-new-window","glyphicon-off","glyphicon-ok","glyphicon-ok-circle","glyphicon-ok-sign","glyphicon-open","glyphicon-paperclip","glyphicon-pause","glyphicon-pencil","glyphicon-phone","glyphicon-phone-alt","glyphicon-picture","glyphicon-plane","glyphicon-play","glyphicon-play-circle","glyphicon-plus","glyphicon-plus-sign","glyphicon-print","glyphicon-pushpin","glyphicon-qrcode","glyphicon-question-sign","glyphicon-random","glyphicon-record","glyphicon-refresh","glyphicon-registration-mark","glyphicon-remove","glyphicon-remove-circle","glyphicon-remove-sign","glyphicon-repeat","glyphicon-resize-full","glyphicon-resize-horizontal","glyphicon-resize-small","glyphicon-resize-vertical","glyphicon-retweet","glyphicon-road","glyphicon-save","glyphicon-saved","glyphicon-screenshot","glyphicon-sd-video","glyphicon-search","glyphicon-send","glyphicon-share","glyphicon-share-alt","glyphicon-shopping-cart","glyphicon-signal","glyphicon-sort","glyphicon-sort-by-alphabet","glyphicon-sort-by-alphabet-alt","glyphicon-sort-by-attributes","glyphicon-sort-by-attributes-alt","glyphicon-sort-by-order","glyphicon-sort-by-order-alt","glyphicon-sound-5-1","glyphicon-sound-6-1","glyphicon-sound-7-1","glyphicon-sound-dolby","glyphicon-sound-stereo","glyphicon-star","glyphicon-star-empty","glyphicon-stats","glyphicon-step-backward","glyphicon-step-forward","glyphicon-stop","glyphicon-subtitles","glyphicon-tag","glyphicon-tags","glyphicon-tasks","glyphicon-text-height","glyphicon-text-width","glyphicon-th","glyphicon-th-large","glyphicon-th-list","glyphicon-thumbs-down","glyphicon-thumbs-up","glyphicon-time","glyphicon-tint","glyphicon-tower","glyphicon-transfer","glyphicon-trash","glyphicon-tree-conifer","glyphicon-tree-deciduous","glyphicon-unchecked","glyphicon-upload","glyphicon-usd","glyphicon-user","glyphicon-volume-down","glyphicon-volume-off","glyphicon-volume-up","glyphicon-warning-sign","glyphicon-wrench","glyphicon-zoom-in","glyphicon-zoom-out","h1","h2","h3","h4","h5","h6","has-error","has-feedback","has-success","has-warning","help-block","hidden","hidden-lg","hidden-md","hidden-print","hidden-sm","hidden-xs","hide","icon-bar","icon-next","icon-prev","img-circle","img-responsive","img-rounded","img-thumbnail","in","info","initialism","input-group","input-group-addon","input-group-btn","input-group-lg","input-group-sm","input-lg","input-sm","invisible","item","jumbotron","label","label-danger","label-default","label-info","label-primary","label-success","label-warning","lead","left","list-group","list-group-item","list-group-item-danger","list-group-item-heading","list-group-item-info","list-group-item-success","list-group-item-text","list-group-item-warning","list-inline","list-unstyled","media","media-body","media-heading","media-list","media-object","modal","modal-backdrop","modal-body","modal-content","modal-dialog","modal-footer","modal-header","modal-lg","modal-open","modal-sm","modal-title","nav","nav-divider","nav-justified","nav-pills","nav-stacked","nav-tabs","nav-tabs-justified","navbar","navbar-brand","navbar-btn","navbar-collapse","navbar-default","navbar-fixed-bottom","navbar-fixed-top","navbar-form","navbar-header","navbar-inverse","navbar-left","navbar-link","navbar-nav","navbar-right","navbar-static-top","navbar-text","navbar-toggle","next","open","page-header","pager","pagination","pagination-lg","pagination-sm","panel","panel-body","panel-collapse","panel-danger","panel-default","panel-footer","panel-group","panel-heading","panel-info","panel-primary","panel-success","panel-title","panel-warning","popover","popover-content","popover-title","pre-scrollable","prev","previous","progress","progress-bar","progress-bar-danger","progress-bar-info","progress-bar-success","progress-bar-warning","progress-striped","pull-left","pull-right","radio","radio-inline","right","row","show","small","sr-only","success","tab-content","tab-pane","table","table-bordered","table-condensed","table-hover","table-responsive","table-striped","text-center","text-danger","text-hide","text-info","text-justify","text-left","text-muted","text-primary","text-right","text-success","text-warning","thumbnail","tooltip","tooltip-arrow","tooltip-inner","top","top-left","top-right","visible-lg","visible-md","visible-print","visible-sm","visible-xs","warning","well","well-lg","well-sm"]



class BootstrapCompletions(sublime_plugin.EventListener):
    """
    Provide tag completions for Bootstrap elements and data-uk attributes
    """
    def __init__(self):

        self.class_completions = [("%s \tBootstrap 3 Class" % s, s) for s in bootstrap_classes]

    def on_query_completions(self, view, prefix, locations):

        if view.match_selector(locations[0], "text.html string.quoted"):

            # Cursor is inside a quoted attribute
            # Now check if we are inside the class attribute

            # max search size
            LIMIT  = 250

            # place search cursor one word back
            cursor = locations[0] - len(prefix) - 1

            # dont start with negative value
            start  = max(0, cursor - LIMIT - len(prefix))

            # get part of buffer
            line   = view.substr(sublime.Region(start, cursor))

            # split attributes
            parts  = line.split('=')

            # is the last typed attribute a class attribute?
            if len(parts) > 1 and parts[-2].strip().endswith("class"):
                return self.class_completions
            else:
                return []
        elif view.match_selector(locations[0], "text.html meta.tag - text.html punctuation.definition.tag.begin"):

            # Cursor is in a tag, but not inside an attribute, i.e. <div {here}>
            # This one is easy, just return completions for the data-uk-* attributes
            return self.data_completions

        else:

            return []
