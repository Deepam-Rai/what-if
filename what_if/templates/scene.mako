<%inherit file="base.mako"/>

<%def name="title()">
    ${node['title']}
</%def>

<%def name="body()">
    <p>${node['text']}</p>

    <div class="choices">
        % for choice in node["choices"]:
            <p><a href="${request.route_url('scene', node=choice['to'])}">
                ${choice["text"]}
            </a></p>
        % endfor
    </div>
</%def>
