{% for field_name,field_obj in fields.items() %} {% set prop_obj = schema.properties.get(field_name) %} {% set dynamic=field_obj.is_dynamic|default(false)%}{%if field_obj.default|default(false)%}{%set wdefault ='(with `'+field_obj.default+'` as default)'%}{%else%}{%set wdefault ='(with no default)'%}{%endif%} {%set descr=field_obj['description'] | default(prop_obj and prop_obj.description|default('(No description provided)')) %}{%set reqd = 'required' if field_obj.required else ('optional ' if 'optional' not in str(field_obj.annotation).lower() else '')%}
* **{{plugin_name}}.{{field_name}}:** *({{reqd}}{{str(field_obj.annotation)}})*
    * {{descr.lstrip()}}
    * Value is {{'**just-in-time**' if dynamic else '**user-configurable**, ' + wdefault}} {%endfor%}
