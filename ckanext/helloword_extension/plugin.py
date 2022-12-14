import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from flask import Blueprint, render_template

def hello_world(name):
    '''A simple view function'''
    return "Hello World, this is an extension called {}".format(name)


class HellowordExtensionPlugin(plugins.SingletonPlugin):
    
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)

    # IConfigurer
    def update_config(self, config_):

        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic',
            'helloword_extension')
            
    #IBlueprint
    def get_blueprint(self):

        # Create Blueprint for plugin
        blueprint = Blueprint(self.name, self.__module__)
        blueprint.template_folder = 'templates'
        # Add plugin url rules to Blueprint object
        blueprint.add_url_rule(
            u'/hello_world/<name>', 
            u'/hello_world', 
            hello_world,
            methods=['GET']
        )
        return blueprint
