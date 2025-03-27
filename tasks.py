from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

## research task

research_task = Task(
    description = (
        "Identify the video {topic}."
        "Get detailed information about the video from the channel."
    ),
    expected_output = "A comprehensive 3 paragraphs long report based on the {topic} of the video content.",
    tools =[yt_tool], 
    agent = blog_researcher,
)

## Writing task with language model configuration

write_task = Task(
    description = (
        "get the info from the youtube channel on the topic {topic}."
    ),
    expected_output = 'Summarize the info from the youtube channel video on the topic{topic} and create the content for the blog',
    tools = [yt_tool],
    agent = blog_writer,
    async_execution = False, ## if we set this to True both agents will be working parallelly
    output_file = 'new-blog-post.md' #Example of output customization
)