<%inherit file="../${context.get('request').registry.settings.get('clld.app_template', 'app.mako')}"/>
<%namespace name="util" file="../util.mako"/>
<%! active_menu_item = "languages" %>

${request.map.render()}

<h2>Language ${ctx.name}</h2>

${request.get_datatable('units', h.models.Unit, language=ctx).render()}
